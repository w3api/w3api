---
title: DatatypeFactory.newInstance()
permalink: /Java/DatatypeFactory/newInstance/
date: 2021-01-11
key: Java.D.DatatypeFactory
category: Java
tags: ['java se', 'javax.xml.datatype', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatatypeFactory.metodos valor="newInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static DatatypeFactory newInstance() throws DatatypeConfigurationException
public static DatatypeFactory newInstance(String factoryClassName, ClassLoader classLoader) throws DatatypeConfigurationException
~~~

## Parámetros
* **ClassLoader classLoader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader classLoader" %}
* **String factoryClassName**,  {% include w3api/param_description.html metodo=_dato parametro="String factoryClassName" %}

## Excepciones
[DatatypeConfigurationException](/Java/DatatypeConfigurationException/)

## Clase Padre
[DatatypeFactory](/Java/DatatypeFactory/)

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
