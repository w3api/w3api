---
title: XPathFactory.newInstance()
permalink: Java/XPathFactory/newInstance
date: 2021-01-04
key: JavaJava.X.XPathFactory
category: java
tags: ['java se', 'javax.xml.xpath', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XPathFactory.metodos valor="newInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static XPathFactory newInstance()
public static XPathFactory newInstance(String uri) throws XPathFactoryConfigurationException
public static XPathFactory newInstance(String uri, String factoryClassName, ClassLoader classLoader) throws XPathFactoryConfigurationException
~~~

## Parámetros
* **ClassLoader classLoader**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader classLoader" %}
* **String factoryClassName**,  {% include w3api/param_description.html metodo=_data parametro="String factoryClassName" %}
* **String uri**,  {% include w3api/param_description.html metodo=_data parametro="String uri" %}

## Excepciones
[XPathFactoryConfigurationException](/Java/XPathFactoryConfigurationException/), [RuntimeException](/Java/RuntimeException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[XPathFactory](/Java/XPathFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XPathFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
