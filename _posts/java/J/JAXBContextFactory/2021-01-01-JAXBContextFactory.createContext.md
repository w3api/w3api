---
title: JAXBContextFactory.createContext()
permalink: /Java/JAXBContextFactory/createContext/
date: 2021-01-11
key: Java.J.JAXBContextFactory
category: Java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 9', 'JAXB 2.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JAXBContextFactory.metodos valor="createContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
JAXBContext createContext(Class<?>[] classesToBeBound, Map<String,?> properties) throws JAXBException
JAXBContext createContext(String contextPath, ClassLoader classLoader, Map<String,?> properties) throws JAXBException
~~~

## Parámetros
* **?&gt; properties**,  {% include w3api/param_description.html metodo=_dato parametro="?> properties" %}
* **ClassLoader classLoader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader classLoader" %}
* **String contextPath**,  {% include w3api/param_description.html metodo=_dato parametro="String contextPath" %}
* **Class&lt;?&gt;[] classesToBeBound**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?>[] classesToBeBound" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [JAXBException](/Java/JAXBException/)

## Clase Padre
[JAXBContextFactory](/Java/JAXBContextFactory/)

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
