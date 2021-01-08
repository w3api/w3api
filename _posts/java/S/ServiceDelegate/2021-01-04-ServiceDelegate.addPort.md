---
title: ServiceDelegate.addPort()
permalink: Java/ServiceDelegate/addPort
date: 2021-01-04
key: JavaJava.S.ServiceDelegate
category: java
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
* **String endpointAddress**,  {% include w3api/param_description.html metodo=_data parametro="String endpointAddress" %}
* **String bindingId**,  {% include w3api/param_description.html metodo=_data parametro="String bindingId" %}
* **QName portName**,  {% include w3api/param_description.html metodo=_data parametro="QName portName" %}

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
{%- for _ldc in site.data.Java.S.ServiceDelegate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
