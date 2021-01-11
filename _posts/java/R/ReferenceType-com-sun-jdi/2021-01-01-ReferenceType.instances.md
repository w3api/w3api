---
title: ReferenceType.instances()
permalink: Java/ReferenceType-com-sun-jdi/instances
date: 2021-01-11
key: JavaJava.R.ReferenceType-com-sun-jdi
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReferenceType-com-sun-jdi.metodos valor="instances" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
List<ObjectReference> instances(long maxInstances)
~~~

## Parámetros
* **long maxInstances**,  {% include w3api/param_description.html metodo=_dato parametro="long maxInstances" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
