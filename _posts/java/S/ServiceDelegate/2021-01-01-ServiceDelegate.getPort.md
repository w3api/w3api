---
title: ServiceDelegate.getPort()
permalink: Java/ServiceDelegate/getPort
date: 2021-01-11
key: JavaJava.S.ServiceDelegate
category: java
tags: ['java se', 'javax.xml.ws.spi', 'java.xml.ws', 'metodo java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceDelegate.metodos valor="getPort" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
abstract <T> T getPort(Class<T> serviceEndpointInterface)
abstract <T> T getPort(Class<T> serviceEndpointInterface, WebServiceFeature... features)
abstract <T> T getPort(QName portName, Class<T> serviceEndpointInterface)
abstract <T> T getPort(QName portName, Class<T> serviceEndpointInterface, WebServiceFeature... features)
abstract <T> T getPort(EndpointReference endpointReference, Class<T> serviceEndpointInterface, WebServiceFeature... features)
~~~

## Parámetros
* **EndpointReference endpointReference**,  {% include w3api/param_description.html metodo=_dato parametro="EndpointReference endpointReference" %}
* **QName portName**,  {% include w3api/param_description.html metodo=_dato parametro="QName portName" %}
* **WebServiceFeature... features**,  {% include w3api/param_description.html metodo=_dato parametro="WebServiceFeature... features" %}
* **Class&lt;T&gt; serviceEndpointInterface**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> serviceEndpointInterface" %}

## Clase Padre
[ServiceDelegate](/Java/ServiceDelegate/)

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
