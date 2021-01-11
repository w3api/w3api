---
title: XMLSignatureFactory.unmarshalXMLSignature()
permalink: Java/XMLSignatureFactory/unmarshalXMLSignature
date: 2021-01-11
key: JavaJava.X.XMLSignatureFactory
category: java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLSignatureFactory.metodos valor="unmarshalXMLSignature" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract XMLSignature unmarshalXMLSignature(XMLValidateContext context) throws MarshalException
public abstract XMLSignature unmarshalXMLSignature(XMLStructure xmlStructure) throws MarshalException
~~~

## Parámetros
* **XMLValidateContext context**,  {% include w3api/param_description.html metodo=_dato parametro="XMLValidateContext context" %}
* **XMLStructure xmlStructure**,  {% include w3api/param_description.html metodo=_dato parametro="XMLStructure xmlStructure" %}

## Excepciones
[MarshalException](/Java/MarshalException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[XMLSignatureFactory](/Java/XMLSignatureFactory/)

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
