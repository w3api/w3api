---
title: SOAPConnection.call()
permalink: /Java/SOAPConnection/call/
date: 2021-01-11
key: Java.S.SOAPConnection
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPConnection.metodos valor="call" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SOAPMessage call(SOAPMessage request, Object to) throws SOAPException
~~~

## Parámetros
* **SOAPMessage request**,  {% include w3api/param_description.html metodo=_dato parametro="SOAPMessage request" %}
* **Object to**,  {% include w3api/param_description.html metodo=_dato parametro="Object to" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[SOAPConnection](/Java/SOAPConnection/)

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
