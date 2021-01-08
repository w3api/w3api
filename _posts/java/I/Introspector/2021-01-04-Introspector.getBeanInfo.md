---
title: Introspector.getBeanInfo()
permalink: Java/Introspector/getBeanInfo
date: 2021-01-04
key: JavaJava.I.Introspector
category: java
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
* **Class&lt;?&gt; stopClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> stopClass" %}
* **int flags**,  {% include w3api/param_description.html metodo=_data parametro="int flags" %}
* **Class&lt;?&gt; beanClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> beanClass" %}

## Excepciones
[IntrospectionException](/Java/IntrospectionException/)

## Clase Padre
[Introspector](/Java/Introspector/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.Introspector.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
