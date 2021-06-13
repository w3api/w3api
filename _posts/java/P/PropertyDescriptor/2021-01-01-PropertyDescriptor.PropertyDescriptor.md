---
title: PropertyDescriptor.PropertyDescriptor()
permalink: /Java/PropertyDescriptor/PropertyDescriptor/
date: 2021-01-11
key: Java.P.PropertyDescriptor
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PropertyDescriptor.constructores valor="PropertyDescriptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PropertyDescriptor(String propertyName, Class<?> beanClass) throws IntrospectionException
public PropertyDescriptor(String propertyName, Class<?> beanClass, String readMethodName, String writeMethodName) throws IntrospectionException
public PropertyDescriptor(String propertyName, Method readMethod, Method writeMethod) throws IntrospectionException
~~~

## Parámetros
* **Method readMethod**,  {% include w3api/param_description.html metodo=_dato parametro="Method readMethod" %}
* **String writeMethodName**,  {% include w3api/param_description.html metodo=_dato parametro="String writeMethodName" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **String readMethodName**,  {% include w3api/param_description.html metodo=_dato parametro="String readMethodName" %}
* **Class&lt;?&gt; beanClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> beanClass" %}
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
