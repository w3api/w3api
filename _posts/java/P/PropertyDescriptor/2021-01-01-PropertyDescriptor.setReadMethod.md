---
title: PropertyDescriptor.setReadMethod()
permalink: /Java/PropertyDescriptor/setReadMethod/
date: 2021-01-11
key: Java.P.PropertyDescriptor
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PropertyDescriptor.metodos valor="setReadMethod" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setReadMethod(Method readMethod) throws IntrospectionException
~~~

## Parámetros
* **Method readMethod**,  {% include w3api/param_description.html metodo=_dato parametro="Method readMethod" %}

## Excepciones
[IntrospectionException](/Java/IntrospectionException/)

## Clase Padre
[PropertyDescriptor](/Java/PropertyDescriptor/)

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
