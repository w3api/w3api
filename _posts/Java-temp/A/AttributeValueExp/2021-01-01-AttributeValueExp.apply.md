---
title: AttributeValueExp.apply()
permalink: /Java/AttributeValueExp/apply/
date: 2021-01-11
key: Java.A.AttributeValueExp
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AttributeValueExp.metodos valor="apply" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ValueExp apply(ObjectName name) throws BadStringOperationException, BadBinaryOpValueExpException, BadAttributeValueExpException, InvalidApplicationException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}

## Excepciones
[BadBinaryOpValueExpException](/Java/BadBinaryOpValueExpException/), [BadAttributeValueExpException](/Java/BadAttributeValueExpException/), [InvalidApplicationException](/Java/InvalidApplicationException/), [BadStringOperationException](/Java/BadStringOperationException/)

## Clase Padre
[AttributeValueExp](/Java/AttributeValueExp/)

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
