---
title: DOMImplementation.createDocument()
permalink: Java/DOMImplementation/createDocument
date: 2021-01-04
key: JavaJava.D.DOMImplementation
category: java
tags: ['java se', 'org.w3c.dom', 'java.xml', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DOMImplementation.metodos valor="createDocument" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Document createDocument(String namespaceURI, String qualifiedName, DocumentType doctype) throws DOMException
~~~

## Parámetros
* **DocumentType doctype**,  {% include w3api/param_description.html metodo=_data parametro="DocumentType doctype" %}
* **String namespaceURI**,  {% include w3api/param_description.html metodo=_data parametro="String namespaceURI" %}
* **String qualifiedName**,  {% include w3api/param_description.html metodo=_data parametro="String qualifiedName" %}

## Excepciones
[DOMException](/Java/DOMException/)

## Clase Padre
[DOMImplementation](/Java/DOMImplementation/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DOMImplementation.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
