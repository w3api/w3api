---
title: ReferenceType.getValue()
permalink: /Java/ReferenceType-com-sun-jdi/getValue/
date: 2021-01-11
key: Java.R.ReferenceType-com-sun-jdi
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReferenceType-com-sun-jdi.metodos valor="getValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Value getValue(Field field)
~~~

## Parámetros
* **Field field**,  {% include w3api/param_description.html metodo=_dato parametro="Field field" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ReferenceType](/Java/ReferenceType-com-sun-jdi/)

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
