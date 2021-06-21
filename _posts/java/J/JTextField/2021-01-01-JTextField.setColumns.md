---
title: JTextField.setColumns()
permalink: /Java/JTextField/setColumns/
date: 2021-01-11
key: Java.J.JTextField
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextField.metodos valor="setColumns" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(bound=false, description="the number of columns preferred for display") public void setColumns(int columns)
~~~

## Parámetros
* **int columns**,  {% include w3api/param_description.html metodo=_dato parametro="int columns" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
