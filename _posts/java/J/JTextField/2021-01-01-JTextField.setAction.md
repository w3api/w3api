---
title: JTextField.setAction()
permalink: /Java/JTextField/setAction/
date: 2021-01-11
key: Java.J.JTextField
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextField.metodos valor="setAction" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(visualUpdate=true, description="the Action instance connected with this ActionEvent source") public void setAction(Action a)
~~~

## Parámetros
* **Action a**,  {% include w3api/param_description.html metodo=_dato parametro="Action a" %}

## Clase Padre
[JTextField](/Java/JTextField/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
