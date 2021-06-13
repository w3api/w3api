---
title: SOAPException.SOAPException()
permalink: /Java/SOAPException/SOAPException/
date: 2021-01-11
key: Java.S.SOAPException
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPException.constructores valor="SOAPException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SOAPException()
public SOAPException(String reason)
public SOAPException(String reason, Throwable cause)
public SOAPException(Throwable cause)
~~~

## Parámetros
* **String reason**,  {% include w3api/param_description.html metodo=_dato parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}

## Clase Padre
[SOAPException](/Java/SOAPException/)

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
