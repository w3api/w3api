---
title: ReferenceType.methodsByName()
permalink: /Java/ReferenceType-com-sun-jdi/methodsByName/
date: 2021-01-11
key: Java.R.ReferenceType-com-sun-jdi
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReferenceType-com-sun-jdi.metodos valor="methodsByName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
List<Method> methodsByName(String name)
List<Method> methodsByName(String name, String signature)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String signature**,  {% include w3api/param_description.html metodo=_dato parametro="String signature" %}

## Excepciones
[ClassNotPreparedException](/Java/ClassNotPreparedException/)

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
