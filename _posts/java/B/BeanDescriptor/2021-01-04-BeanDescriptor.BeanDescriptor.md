---
title: BeanDescriptor.BeanDescriptor()
permalink: Java/BeanDescriptor/BeanDescriptor
date: 2021-01-04
key: JavaJava.B.BeanDescriptor
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanDescriptor.constructores valor="BeanDescriptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BeanDescriptor(Class<?> beanClass)
public BeanDescriptor(Class<?> beanClass, Class<?> customizerClass)
~~~

## Parámetros
* **Class&lt;?&gt; customizerClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> customizerClass" %}
* **Class&lt;?&gt; beanClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> beanClass" %}

## Clase Padre
[BeanDescriptor](/Java/BeanDescriptor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BeanDescriptor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
