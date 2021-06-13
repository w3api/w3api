---
title: XMLEventFactory.newInstance()
permalink: /Java/XMLEventFactory/newInstance/
date: 2021-01-11
key: Java.X.XMLEventFactory
category: Java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLEventFactory.metodos valor="newInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static XMLEventFactory newInstance() throws FactoryConfigurationError
@Deprecated(since="1.7") public static XMLEventFactory newInstance(String factoryId, ClassLoader classLoader) throws FactoryConfigurationError
~~~

## Parámetros
* **String factoryId**,  {% include w3api/param_description.html metodo=_dato parametro="String factoryId" %}
* **ClassLoader classLoader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader classLoader" %}

## Clase Padre
[XMLEventFactory](/Java/XMLEventFactory/)

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
