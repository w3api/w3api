---
title: StartTlsRequest.createExtendedResponse()
permalink: /Java/StartTlsRequest/createExtendedResponse/
date: 2021-01-11
key: Java.S.StartTlsRequest
category: Java
tags: ['java se', 'javax.naming.ldap', 'java.naming', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StartTlsRequest.metodos valor="createExtendedResponse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ExtendedResponse createExtendedResponse(String id, byte[] berValue, int offset, int length) throws NamingException
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **byte[] berValue**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] berValue" %}
* **String id**,  {% include w3api/param_description.html metodo=_dato parametro="String id" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[StartTlsRequest](/Java/StartTlsRequest/)

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
