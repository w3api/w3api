---
title: SOAPMessage.getProperty()
permalink: /Java/SOAPMessage/getProperty/
date: 2021-01-11
key: Java.S.SOAPMessage
category: Java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPMessage.metodos valor="getProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getProperty(String property) throws SOAPException
~~~

## Parámetros
* **String property**,  {% include w3api/param_description.html metodo=_dato parametro="String property" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[SOAPMessage](/Java/SOAPMessage/)

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
