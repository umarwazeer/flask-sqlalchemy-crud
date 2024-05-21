from flask import Flask, jsonify, request
from app import app, db
from models.employee import Employee, User


@app.route('/employees', methods=['GET'])
# Get all Employee
def get_emp():
    users = Employee.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 
     'email': user.email, 
    #  'dep_id': user.dep.name,
    #  'salary': user.salary,
      'role': user.role, 'phone': user.phone, 'gender': user.gender} for user in users])


# Get by is employee
@app.route('/employees/<int:id>', methods=['GET']) 
def get_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'})
    result = {'id': employee.id, 'name': employee.name, 'email': employee.email, 'salary': employee.salary}
    return jsonify(result)

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_employee = Employee(
            name=data['name'],
            # dep_id=data['id'],
            email=data['email'],
            salary=data['salary'],
            role=data['role'],
            phone=data['phone'],
            gender=data['gender']
            )

    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'id': new_employee.id, 'name': new_employee.name, 'email': new_employee.email,
    #  'dep_id': new_user.dep_id,
      'salary': new_employee.salary
      }), 201

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'})
    data = request.get_json()
    employee.name = data['name']
    employee.email = data['email']
    employee.salary = data['salary']
    db.session.commit()
    return jsonify({'message': 'Employee updated'})

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'message': 'Employee not found'})
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted'})

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name, 
    'email': user.email, 
    # 'depaprtment': user.dep.name,
     'image':user.image} for user in users])

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User not found'})
    result = {'id': user.id, 'username': user.name, 'email': user.email}
    return jsonify(result)


# Delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200


@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added'})

    
# Update a Employee
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 200




