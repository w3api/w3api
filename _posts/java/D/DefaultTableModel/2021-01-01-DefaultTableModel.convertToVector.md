---
title: DefaultTableModel.convertToVector()
permalink: Java/DefaultTableModel/convertToVector
date: 2021-01-11
key: JavaJava.D.DefaultTableModel
category: java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultTableModel.metodos valor="convertToVector" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected static Vector<Object> convertToVector(Object[] anArray)
protected static Vector<Vector<Object>> convertToVector(Object[][] anArray)
~~~

## Parámetros
* **Object[] anArray**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] anArray" %}
* **Object[][] anArray**,  {% include w3api/param_description.html metodo=_dato parametro="Object[][] anArray" %}

## Clase Padre
[DefaultTableModel](/Java/DefaultTableModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
