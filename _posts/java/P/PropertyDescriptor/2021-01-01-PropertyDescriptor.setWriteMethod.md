---
title: PropertyDescriptor.setWriteMethod()
permalink: /Java/PropertyDescriptor/setWriteMethod/
date: 2021-01-11
key: Java.P.PropertyDescriptor
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PropertyDescriptor.metodos valor="setWriteMethod" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setWriteMethod(Method writeMethod) throws IntrospectionException
~~~

## Parámetros
* **Method writeMethod**,  {% include w3api/param_description.html metodo=_dato parametro="Method writeMethod" %}

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
