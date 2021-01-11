---
title: JMXServiceURL.JMXServiceURL()
permalink: Java/JMXServiceURL/JMXServiceURL
date: 2021-01-11
key: JavaJava.J.JMXServiceURL
category: java
tags: ['java se', 'javax.management.remote', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMXServiceURL.constructores valor="JMXServiceURL" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JMXServiceURL(String serviceURL) throws MalformedURLException
public JMXServiceURL(String protocol, String host, int port) throws MalformedURLException
public JMXServiceURL(String protocol, String host, int port, String urlPath) throws MalformedURLException
~~~

## Parámetros
* **String host**,  {% include w3api/param_description.html metodo=_dato parametro="String host" %}
* **String serviceURL**,  {% include w3api/param_description.html metodo=_dato parametro="String serviceURL" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **String urlPath**,  {% include w3api/param_description.html metodo=_dato parametro="String urlPath" %}
* **String protocol**,  {% include w3api/param_description.html metodo=_dato parametro="String protocol" %}

## Excepciones
[MalformedURLException](/Java/MalformedURLException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[JMXServiceURL](/Java/JMXServiceURL/)

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
