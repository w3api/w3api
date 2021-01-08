---
title: SOAPElement.addNamespaceDeclaration()
permalink: Java/SOAPElement/addNamespaceDeclaration
date: 2021-01-04
key: JavaJava.S.SOAPElement
category: java
tags: ['java se', 'javax.xml.soap', 'java.xml.ws', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SOAPElement.metodos valor="addNamespaceDeclaration" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SOAPElement addNamespaceDeclaration(String prefix, String uri) throws SOAPException
~~~

## Parámetros
* **String prefix**,  {% include w3api/param_description.html metodo=_data parametro="String prefix" %}
* **String uri**,  {% include w3api/param_description.html metodo=_data parametro="String uri" %}

## Excepciones
[SOAPException](/Java/SOAPException/)

## Clase Padre
[SOAPElement](/Java/SOAPElement/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SOAPElement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
