---
title: Introspector.getBeanInfo()
permalink: /Java/Introspector/getBeanInfo/
date: 2021-01-11
key: Java.I.Introspector
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.Introspector.metodos valor="getBeanInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static BeanInfo getBeanInfo(Class<?> beanClass) throws IntrospectionException
public static BeanInfo getBeanInfo(Class<?> beanClass, int flags) throws IntrospectionException
public static BeanInfo getBeanInfo(Class<?> beanClass, Class<?> stopClass) throws IntrospectionException
public static BeanInfo getBeanInfo(Class<?> beanClass, Class<?> stopClass, int flags) throws IntrospectionException
~~~

## Parámetros
* **int flags**,  {% include w3api/param_description.html metodo=_dato parametro="int flags" %}
* **Class&lt;?&gt; stopClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> stopClass" %}
* **Class&lt;?&gt; beanClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> beanClass" %}

## Excepciones
[IntrospectionException](/Java/IntrospectionException/)

## Clase Padre
[Introspector](/Java/Introspector/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
