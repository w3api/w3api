---
title: SOAPHeader.addUpgradeHeaderElement()
permalink: Java/SOAPHeader/addUpgradeHeaderElement
date: 2021-01-11
key: JavaJava.S.SOAPHeader
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPHeader.metodos valor="addUpgradeHeaderElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SOAPHeaderElement addUpgradeHeaderElement(String supportedSoapUri) throws SOAPException
SOAPHeaderElement addUpgradeHeaderElement(String[] supportedSoapUris) throws SOAPException
SOAPHeaderElement addUpgradeHeaderElement(Iterator<String> supportedSOAPURIs) throws SOAPException
~~~

## Parámetros
* **String supportedSoapUri**,  {% include w3api/param_description.html metodo=_dato parametro="String supportedSoapUri" %}
* **Iterator&lt;String&gt; supportedSOAPURIs**,  {% include w3api/param_description.html metodo=_dato parametro="Iterator<String> supportedSOAPURIs" %}
* **String[] supportedSoapUris**,  {% include w3api/param_description.html metodo=_dato parametro="String[] supportedSoapUris" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[SOAPHeader](/Java/SOAPHeader/)

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
