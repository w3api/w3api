---
title: JAXBContextFactory.createContext()
permalink: Java/JAXBContextFactory/createContext
date: 2021-01-04
key: JavaJava.J.JAXBContextFactory
category: java
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
* **String contextPath**,  {% include w3api/param_description.html metodo=_data parametro="String contextPath" %}
* **Class&lt;?&gt;[] classesToBeBound**,  {% include w3api/param_description.html metodo=_data parametro="Class<?>[] classesToBeBound" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **?&gt; properties**,  {% include w3api/param_description.html metodo=_data parametro="?> properties" %}
* **ClassLoader classLoader**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader classLoader" %}

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
{%- for _ldc in site.data.Java.J.JAXBContextFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
