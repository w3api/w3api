---
title: PropertyDescriptor.PropertyDescriptor()
permalink: Java/PropertyDescriptor/PropertyDescriptor
date: 2021-01-04
key: JavaJava.P.PropertyDescriptor
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
* **String writeMethodName**,  {% include w3api/param_description.html metodo=_data parametro="String writeMethodName" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}
* **Method writeMethod**,  {% include w3api/param_description.html metodo=_data parametro="Method writeMethod" %}
* **Method readMethod**,  {% include w3api/param_description.html metodo=_data parametro="Method readMethod" %}
* **String readMethodName**,  {% include w3api/param_description.html metodo=_data parametro="String readMethodName" %}
* **Class&lt;?&gt; beanClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> beanClass" %}

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
{%- for _ldc in site.data.Java.P.PropertyDescriptor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
