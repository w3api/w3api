---
title: ServiceDelegate.addPort()
permalink: /Java/ServiceDelegate/addPort/
date: 2021-01-11
key: Java.S.ServiceDelegate
category: Java
tags: ['java se', 'javax.xml.ws.spi', 'java.xml.ws', 'metodo java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceDelegate.metodos valor="addPort" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void addPort(QName portName, String bindingId, String endpointAddress)
~~~

## Parámetros
* **QName portName**,  {% include w3api/param_description.html metodo=_dato parametro="QName portName" %}
* **String endpointAddress**,  {% include w3api/param_description.html metodo=_dato parametro="String endpointAddress" %}
* **String bindingId**,  {% include w3api/param_description.html metodo=_dato parametro="String bindingId" %}

## Excepciones
[WebServiceException](/Java/WebServiceException/)

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
