---
title: DeclHandler.attributeDecl()
permalink: Java/DeclHandler/attributeDecl
date: 2021-01-11
key: JavaJava.D.DeclHandler
category: java
tags: ['java se', 'org.xml.sax.ext', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0 (extensions Java 1.0)']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DeclHandler.metodos valor="attributeDecl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void attributeDecl(String eName, String aName, String type, String mode, String value) throws SAXException
~~~

## Parámetros
* **String mode**,  {% include w3api/param_description.html metodo=_dato parametro="String mode" %}
* **String value**,  {% include w3api/param_description.html metodo=_dato parametro="String value" %}
* **String eName**,  {% include w3api/param_description.html metodo=_dato parametro="String eName" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}
* **String aName**,  {% include w3api/param_description.html metodo=_dato parametro="String aName" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[DeclHandler](/Java/DeclHandler/)

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
