---
title: IndexedPropertyDescriptor.IndexedPropertyDescriptor()
permalink: /Java/IndexedPropertyDescriptor/IndexedPropertyDescriptor/
date: 2021-01-11
key: Java.I.IndexedPropertyDescriptor
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IndexedPropertyDescriptor.constructores valor="IndexedPropertyDescriptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public IndexedPropertyDescriptor(String propertyName, Class<?> beanClass) throws IntrospectionException
public IndexedPropertyDescriptor(String propertyName, Class<?> beanClass, String readMethodName, String writeMethodName, String indexedReadMethodName, String indexedWriteMethodName) throws IntrospectionException
public IndexedPropertyDescriptor(String propertyName, Method readMethod, Method writeMethod, Method indexedReadMethod, Method indexedWriteMethod) throws IntrospectionException
~~~

## Parámetros
* **String indexedWriteMethodName**,  {% include w3api/param_description.html metodo=_dato parametro="String indexedWriteMethodName" %}
* **Method readMethod**,  {% include w3api/param_description.html metodo=_dato parametro="Method readMethod" %}
* **String writeMethodName**,  {% include w3api/param_description.html metodo=_dato parametro="String writeMethodName" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **String readMethodName**,  {% include w3api/param_description.html metodo=_dato parametro="String readMethodName" %}
* **Method indexedReadMethod**,  {% include w3api/param_description.html metodo=_dato parametro="Method indexedReadMethod" %}
* **Class&lt;?&gt; beanClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> beanClass" %}
* **Method writeMethod**,  {% include w3api/param_description.html metodo=_dato parametro="Method writeMethod" %}
* **String indexedReadMethodName**,  {% include w3api/param_description.html metodo=_dato parametro="String indexedReadMethodName" %}
* **Method indexedWriteMethod**,  {% include w3api/param_description.html metodo=_dato parametro="Method indexedWriteMethod" %}

## Excepciones
[IntrospectionException](/Java/IntrospectionException/)

## Clase Padre
[IndexedPropertyDescriptor](/Java/IndexedPropertyDescriptor/)

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
