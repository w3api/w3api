---
title: XMLOutputFactory.newFactory()
permalink: /Java/XMLOutputFactory/newFactory/
date: 2021-01-11
key: Java.X.XMLOutputFactory
category: Java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLOutputFactory.metodos valor="newFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static XMLOutputFactory newFactory() throws FactoryConfigurationError
public static XMLOutputFactory newFactory(String factoryId, ClassLoader classLoader) throws FactoryConfigurationError
~~~

## Parámetros
* **String factoryId**,  {% include w3api/param_description.html metodo=_dato parametro="String factoryId" %}
* **ClassLoader classLoader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader classLoader" %}

## Clase Padre
[XMLOutputFactory](/Java/XMLOutputFactory/)

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
