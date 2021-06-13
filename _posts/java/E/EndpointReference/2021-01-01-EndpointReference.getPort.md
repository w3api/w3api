---
title: EndpointReference.getPort()
permalink: /Java/EndpointReference/getPort/
date: 2021-01-11
key: Java.E.EndpointReference
category: Java
tags: ['java se', 'javax.xml.ws', 'java.xml.ws', 'metodo java', 'Java 1.6', 'JAX-WS 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EndpointReference.metodos valor="getPort" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T> T getPort(Class<T> serviceEndpointInterface, WebServiceFeature... features)
~~~

## Parámetros
* **WebServiceFeature... features**,  {% include w3api/param_description.html metodo=_dato parametro="WebServiceFeature... features" %}
* **Class&lt;T&gt; serviceEndpointInterface**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> serviceEndpointInterface" %}

## Clase Padre
[EndpointReference](/Java/EndpointReference/)

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
