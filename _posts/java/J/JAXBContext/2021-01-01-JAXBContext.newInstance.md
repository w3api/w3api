---
title: JAXBContext.newInstance()
permalink: Java/JAXBContext/newInstance
date: 2021-01-11
key: JavaJava.J.JAXBContext
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JAXBContext.metodos valor="newInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static JAXBContext newInstance(Class<?>... classesToBeBound) throws JAXBException
public static JAXBContext newInstance(Class<?>[] classesToBeBound, Map<String,?> properties) throws JAXBException
public static JAXBContext newInstance(String contextPath) throws JAXBException
public static JAXBContext newInstance(String contextPath, ClassLoader classLoader) throws JAXBException
public static JAXBContext newInstance(String contextPath, ClassLoader classLoader, Map<String,?> properties) throws JAXBException
~~~

## Parámetros
* **?&gt; properties**,  {% include w3api/param_description.html metodo=_dato parametro="?> properties" %}
* **ClassLoader classLoader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader classLoader" %}
* **Class&lt;?&gt;... classesToBeBound**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?>... classesToBeBound" %}
* **String contextPath**,  {% include w3api/param_description.html metodo=_dato parametro="String contextPath" %}
* **Class&lt;?&gt;[] classesToBeBound**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?>[] classesToBeBound" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [JAXBException](/Java/JAXBException/)

## Clase Padre
[JAXBContext](/Java/JAXBContext/)

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
