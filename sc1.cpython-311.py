�
    A1�eY$  �                   �   � d dl mZ d dlZd dlmZmZmZ d dlZd dlZd dl	Z	 ed��  �         d dl
Z
d dl
mZmZ ddd	d
dddddddd�Z ej        e�  �        Z e
j        e�  �          ej        �   �         Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zd� Zedk    rjej        � ej        � �Zedz  Z ee�  �          ej        d�  �        Z  ee �  �        r ej!         e�   �         �  �         dS  eej"        � d��  �         dS dS )�    )�ClientN)�Fore�Style�initT)�	autoreset)�credentials�	firestore�service_accountzbanded-lexicon-374509�(9faef72167d99fcfb63810d736cd2c9777deeb59a�  -----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDAjQYXJ7SCS1RW
wiiD2SfEAv8am6N33DFBTFqAZxTsp+tTY8N/xSYhbn3BkTzfJvJI2rflc+5DVH03
MYAROp+6R45UETIJ2nRylGNw9IXVZDGLhUUWyLPSbclnxHfVWRsz26dBR/gr1o2m
IXk2jqQ69H9mf1SwNuzry0NCdPT6FjAps50csumMZWejkdsz7vHH7YG7rEQZGaLs
xGCl5AZ7puReULeeGDD1PzsZl/88KiPD0mNjFbDHgeyOeaTGkaesli8iCrLiHrhp
yS2iHfQ+xmZLZ6HFSf4KfrHam3tRwr7JVGlNp3knAjChQOk4tCcSBN6Ox0SRT8mt
SDfkujljAgMBAAECggEAI16kVEOMYnTA8NDojVOp/NUKFFKro/xUJekHJNgKnXA5
B4/nXQSTfQelXRW3R0yJq/1VU3ZIuaB/AdD7c+6/YYH8cI/aD7pLsrJ0U87u+KRX
f4gDCWzjr09QdFnAI3YjS5LZNeIpAbB/Q5mZgP6Rx2ybLHJOVbI5MhUb7Uy7pWZ0
8E4+qUA8TgsISOS0X3iTv40hjgbCDUpAZc8WSgTcrD1ikjkPgehNtXpGkxMK5x8o
iiW27ErP+ktsAK5HsLN+SA954rhim5RTO2evZWFNAOEyxw14/BTFLpW/jHItkR0L
M4Oe9ORq/V1EMKBe/absA11+BS4OlvXfc/ToyLy6XQKBgQD3/qDYvLNvBRziC8u+
IgNQnGEtSO00TeBPN3+ooj0ONTP+X0z/s2zo/ccLOLG7M9Exmdmc/q1Bn2MNC6PO
gD0YZ5bJmnDWN42IMrzuojeCtmFPF003O5YK+Zin98UGITNY9PPWRcoErfeu0hom
0kDJ5zgAbAjVqiW0CSJ5iwRehwKBgQDGxDiAsumuQrI2jVKCwYoU9LVAmAnnDzvi
rA+ba8t9EtkJ69dawUJgvAtiC8yhkwbLoAUFrVIsrgICkH37o07fISZa/Rh6Y+0G
lWyUzY0D+1QYsoeRtQO4TY8NBMAxY+x1M/pzBAz2tzGJu5NY3yHJl4Scf08rHr3W
GsyNdXYJRQKBgQCAmcFNQ2WFH9Cfg+Buw3KWndFiy1t+cRft3GjNyPwCXyKMOV1T
h/blR5ytPAQmgLNtlkubtxGfYwjZXfze++8ytZ0jBHyZCYvSYgVJdkN0/CCwA/Rd
vP+Mx2wbRkgcaqEW80dzCRO+o3w6Yud+1C8WxFltFpjqO+Z7WvVOtAFbBwKBgCqy
b+jFhgkW7q1lQjowVPcXcfAEOOxXi2evylJ6n2WorNLCxKoMJbQd8NwI6NY0fRs0
rp9/kc1jO69NVqK9e+3WcyTMhXuVB4+IfaChXw9h57i+cPzNw5TNpFMJmDeD3YF3
vu8CCb7dr1iE4KwQknN5htUPS/RZUDIz44jnmIl5AoGAdUaiIuKuKkgEIpz0Bi37
//bBJgupH4SVM9+kyDbQGKlprrPT/AiH9nQgfhiLRqVTbOMtBjQcaa5sJQunejWX
J5XcusI2mi/+r/x1izpzayO2iD+/UZJ1Q/7KppaQSy+c6nBoQjwtx0WuwdKR6AG7
EFdMffj90gYd9FrnAmSSV9E=
-----END PRIVATE KEY-----
zEfirebase-adminsdk-iqopq@banded-lexicon-374509.iam.gserviceaccount.com�106157612129827927729z)https://accounts.google.com/o/oauth2/authz#https://oauth2.googleapis.com/tokenz*https://www.googleapis.com/oauth2/v1/certszyhttps://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-iqopq%40banded-lexicon-374509.iam.gserviceaccount.comzgoogleapis.com)�type�
project_id�private_key_id�private_key�client_email�	client_id�auth_uri�	token_uri�auth_provider_x509_cert_url�client_x509_cert_url�universe_domainc                  �    � t          d�  �        �)Nz8No authorization key provided. Please enter a valid key.)�	Exception� �    �./sc1.py�generate_auth_keyr      s   � �
�N�
O�
O�Or   c                 �  � |�                     �   �         }|j        rRd|�                    �   �         v r<|�                    �   �         �                     d�  �        | k    rt          d�  �        �d S |�                    d| i�  �         d S )N�	device_idz1Different Device ID already present on the server)�get�exists�to_dictr   �update)r   �doc_ref�docs      r   �store_device_idr&   !   s�   � �
�+�+�-�-�C�
�z� 1�k�S�[�[�]�]�2�2��;�;�=�=���[�)�)�Y�6�6��O�P�P�P� 7�6� 	����Y�/�0�0�0�0�0r   c                 �.  � t          t          j        �   �         �  �        }t          �                    d�  �        �                    �   �         }|D ]E}|�                    �   �         �                    d�  �        | k    rt          ||j	        �  �          dS �FdS )N�passes�authTF)
�str�uuid�getnode�db�
collection�streamr"   r    r&   �	reference)�auth_keyr   �docsr%   s       r   �validate_auth_keyr3   )   s�   � ��D�L�N�N�#�#�I��=�=��"�"�)�)�+�+�D�� � ���;�;�=�=���V�$�$��0�0��I�s�}�5�5�5��4�4� 1� �5r   c              �   �   K  � g }| �                     �   �         2 3 d {V ��}|�                    |j        j        �  �         d� |D �   �         }d� |D �   �         }�?6 |S )Nc                 �p   � g | ]3}t          |�  �        �                    d �  �        �$t          |�  �        ��4S )�-)r*   �
startswith��.0�chat_ids     r   �
<listcomp>z get_chat_ids.<locals>.<listcomp>6   s8   � �Y�Y�Y�W�C��L�L�<S�<S�TW�<X�<X�Y�C��L�L�Y�Y�Yr   c                 �,   � g | ]}t          |�  �        ��S r   )�intr8   s     r   r;   z get_chat_ids.<locals>.<listcomp>7   s   � �9�9�9�W�C��L�L�9�9�9r   )�get_dialogs�append�chat�id)�app�chat_ids�dialogs      r   �get_chat_idsrE   2   s�   � � � ��H����)�)� :� :� :� :� :� :� :�f�������'�'�'�Y�Y��Y�Y�Y��9�9��9�9�9��� *� �Os   �Ac              �   �\   ���K  � ��fd��t          j        �fd�| D �   �         � � d {V �� d S )Nc           
   �   �  �K  � t          | �  �        � d {V ��}t          ��  �        D �].}	 | �                    dd��  �        2 3 d {V ��}|j        } n6 n7# t          $ r*}t          t          j        � d|� ��  �         d }Y d }~nd }~ww xY w|��|D ]�}	 | �                    |d|�  �        � d {V �� t          t          j	        � d|� ��  �         t          j        d�  �        � d {V �� n8# t          $ r+}t          t          j        � d|� d|� ��  �         Y d }~nd }~ww xY wt          j        d	�  �        � d {V �� ��t          j        ��  �        � d {V �� ��0d S )
N�me�   )�limitzFailed to fetch last message: zMessage sent to chat_id �   z"Failed to send message to chat_id �: �   )rE   �range�get_chat_historyrA   r   �printr   �RED�forward_messages�GREEN�asyncio�sleep)	rB   rC   �i�message�last_message�er:   �numtime�timees	          ��r   �send_last_messagez6send_last_message_to_groups.<locals>.send_last_message;   s  �� � � �%�c�*�*�*�*�*�*�*�*���w��� 	'� 	'�A�$�%(�%9�%9�$�a�%9�%H�%H� � � � � � � �'�#*�:�L��E� &I��� � $� $� $����D�D��D�D�E�E�E�#�����������$���� �'�'� +� +�G�]�!�2�2�7�D�,�O�O�O�O�O�O�O�O�O����N�N�W�N�N�O�O�O�%�m�A�.�.�.�.�.�.�.�.�.�.��$� ]� ]� ]����[�[�W�[�[�XY�[�[�\�\�\�\�\�\�\�\�����]����!�-��*�*�*�*�*�*�*�*�*�*��-��&�&�&�&�&�&�&�&�&�&�'	'� 	's<   �A�A�	A�
B	� B�B	�AC)�)
D�3!D�Dc              3   �.   �K  � | ]} �|�  �        V � �d S )Nr   )r9   rB   r\   s     �r   �	<genexpr>z.send_last_message_to_groups.<locals>.<genexpr>R   s/   �� � � �B�B�c�,�,�S�1�1�B�B�B�B�B�Br   )rT   �gather)�appsr[   rZ   r\   s    ``@r   �send_last_message_to_groupsra   :   sc   ���� � � �'� '� '� '� '� '�. �.�B�B�B�B�T�B�B�B�
C�C�C�C�C�C�C�C�C�Cr   c           	   �   ��   K  � |D ]t}	 | �                     |�  �        � d {V �� t          t          j        � d|� ��  �         �=# t          $ r+}t          t          j        � d|� d|� ��  �         Y d }~�md }~ww xY wd S )NzLeft chat_id zFailed to leave chat_id rL   )�
leave_chatrP   r   �CYANr   rQ   )rB   rC   r:   rY   s       r   �leave_chatsre   T   s�   � � � �� G� G��	G��.�.��)�)�)�)�)�)�)�)�)��T�Y�6�6�W�6�6�7�7�7�7��� 	G� 	G� 	G��T�X�E�E�w�E�E�!�E�E�F�F�F�F�F�F�F�F�����	G����	G� Gs   �9A�
A7�!A2�2A7c              �   ��   K  � 	 | �                     |�  �        � d {V �� t          t          j        � d|� ��  �         d S # t          $ r,}t          t          j        � d|� d|� ��  �         Y d }~d S d }~ww xY w)NzJoined chat_id zFailed to join chat_id rL   )�	join_chatrP   r   �MAGENTAr   rQ   )rB   r:   rY   s      r   �
join_groupri   \   s�   � � � �B��m�m�G�$�$�$�$�$�$�$�$�$����7�7�g�7�7�8�8�8�8�8��� B� B� B����@�@�'�@�@�Q�@�@�A�A�A�A�A�A�A�A�A�����B���s   �9? �
A5�	!A0�0A5c            	   �   �  K  � t          t          d�  �        �  �        } g }t          | �  �        D ]�}d|dz   � �}	 t          |�  �        }|�                    �   �         � d {V �� nf#  t          t          d|� d��  �        �  �        }t          d|� d��  �        }t          |||��  �        }|�                    �   �         � d {V �� Y nxY w|�                    |�  �         ��	 t          t          t          j        � t          j	        � d	t          j
        � ��  �        �  �        }|d
k    rPt          t          d�  �        �  �        }t          t          d�  �        �  �        }	t          ||	|�  �        � d {V �� n�|dk    r+|D ]'}t          d�  �        }
t          ||
�  �        � d {V �� �(n�|dk    r1|D ]-}t          |�  �        � d {V ��}t          ||�  �        � d {V �� �.nx|dk    rKt          d�  �        }t          |�  �        � d {V ��}|D ]#}
|D ]}|�                    |
|�  �        � d {V �� ��$n'|dk    r!|D ]}|�                    �   �         � d {V �� �d S ��y)NzEnter the number of sessions: �
my_accountrI   zEnter api id for rL   zEnter api_hash for )�api_id�api_hashTz�2. AutoSender
3. Auto Group Joiner
4. Leave all groups
5. Add user to all groups(will only work with one login)
6. Exit
Enter the choice: rK   z-How many times you want to send the message: zEnter the time delay: �   zEnter the Chat ID to join: �   rM   z(Enter the user ID to add to all groups: �   )r=   �inputrN   r   �startr?   r   �BRIGHTr   �YELLOW�	RESET_ALLra   ri   rE   re   �add_chat_members�stop)�num_sessionsr`   rV   �session_namerB   rl   rm   �arZ   r[   r:   rC   �user_ids                r   �mainr|   d   sO  � � � ��u�=�>�>�?�?�L��D��<� � � � ��)�A�a�C�)�)��		���&�&�C��)�)�+�+����������	���C�<�C�C�C�D�D�E�E�F��C�<�C�C�C�D�D�H���f�x�H�H�H�C��)�)�+�+����������������C�����#����|�  K�T�[�  K�  K�  z�  zI�  K�  K�
� 
� � �� ��6�6��%� O�P�P�Q�Q�G���6�7�7�8�8�E�-�d�E�7�C�C�C�C�C�C�C�C�C�C��!�V�V�� /� /��� =�>�>�� ��g�.�.�.�.�.�.�.�.�.�.�/� �!�V�V�� 1� 1��!-�c�!2�!2�2�2�2�2�2�2��!�#�x�0�0�0�0�0�0�0�0�0�0�1� �!�V�V��F�G�G�G�)�#�.�.�.�.�.�.�.�.�H�#� A� A��� A� A�C��.�.�w��@�@�@�@�@�@�@�@�@�@�A�A� �!�V�V�� !� !���h�h�j�j� � � � � � � � ��E�G#s   �)A%�%A!C�__main__a-  
     _____                               _______                    _                        _             
    |  __ \                             |__   __|        /\        | |                      | |            
    | |  | | ___ _ __ ___   ___  _ __      | | __ _     /  \  _   _| |_ ___  _ __ ___   __ _| |_ ___  _ __ 
    | |  | |/ _ \ '_ ` _ \ / _ \| '_ \     | |/ _` |   / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __/ _ \| '__|
    | |__| |  __/ | | | | | (_) | | | |    | | (_| |  / ____ \ |_| | || (_) | | | | | | (_| | || (_) | |   
    |_____/ \___|_| |_| |_|\___/|_| |_|    |_|\__, | /_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__\___/|_|   
                                               __/ |                                                       
                                              |___/
    zEnter your authorization key: zInvalid auth key!!
Exiting.....)#�pyrogramr   rT   �coloramar   r   r   �requests�getpassr+   �firebase_adminr   r	   �firebase_credentials�Certificate�cred�initialize_app�clientr-   r   r&   r3   rE   ra   re   ri   r|   �__name__rd   rs   �stytextrP   r1   �runrQ   r   r   r   �<module>r�      s0  �� � � � � � � ���� &� &� &� &� &� &� &� &� &� &� ���� ���� ���� ��t� � � � � � � � � 1� 1� 1� 1� 1� 1� 1� 1� �)�@� Z�[�(�;�6�#O� X�'�� � � �{��3�4�4�� �� �d� #� #� #��Y�����P� P� P�1� 1� 1�� � �� � �D� D� D�4G� G� G�B� B� B�5� 5� 5�n �z�����*�E�L�*�*�G�� 	� 	�G� 
�E�'�N�N�N��w��?�@�@�H� ���"�"� =����D�D�F�F����������;�;�;�<�<�<�<�<�) �r   