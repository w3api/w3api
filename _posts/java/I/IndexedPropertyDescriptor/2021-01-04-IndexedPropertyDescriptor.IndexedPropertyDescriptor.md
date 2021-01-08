---
title: IndexedPropertyDescriptor.IndexedPropertyDescriptor()
permalink: Java/IndexedPropertyDescriptor/IndexedPropertyDescriptor
date: 2021-01-04
key: JavaJava.I.IndexedPropertyDescriptor
category: java
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
* **String writeMethodName**,  {% include w3api/param_description.html metodo=_data parametro="String writeMethodName" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}
* **Method indexedReadMethod**,  {% include w3api/param_description.html metodo=_data parametro="Method indexedReadMethod" %}
* **Method writeMethod**,  {% include w3api/param_description.html metodo=_data parametro="Method writeMethod" %}
* **Method indexedWriteMethod**,  {% include w3api/param_description.html metodo=_data parametro="Method indexedWriteMethod" %}
* **Method readMethod**,  {% include w3api/param_description.html metodo=_data parametro="Method readMethod" %}
* **String indexedReadMethodName**,  {% include w3api/param_description.html metodo=_data parametro="String indexedReadMethodName" %}
* **String indexedWriteMethodName**,  {% include w3api/param_description.html metodo=_data parametro="String indexedWriteMethodName" %}
* **String readMethodName**,  {% include w3api/param_description.html metodo=_data parametro="String readMethodName" %}
* **Class&lt;?&gt; beanClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> beanClass" %}

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
{%- for _ldc in site.data.Java.I.IndexedPropertyDescriptor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
