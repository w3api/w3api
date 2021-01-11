---
title: JAXBElement.JAXBElement()
permalink: Java/JAXBElement/JAXBElement
date: 2021-01-11
key: JavaJava.J.JAXBElement
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JAXBElement.constructores valor="JAXBElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JAXBElement(QName name, Class<T> declaredType, Class scope, T value)
public JAXBElement(QName name, Class<T> declaredType, T value)
~~~

## Parámetros
* **QName name**,  {% include w3api/param_description.html metodo=_dato parametro="QName name" %}
* **Class scope**,  {% include w3api/param_description.html metodo=_dato parametro="Class scope" %}
* **Class&lt;T&gt; declaredType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> declaredType" %}
* **T value**,  {% include w3api/param_description.html metodo=_dato parametro="T value" %}

## Clase Padre
[JAXBElement](/Java/JAXBElement/)

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
