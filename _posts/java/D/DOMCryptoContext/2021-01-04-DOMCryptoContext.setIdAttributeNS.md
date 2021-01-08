---
title: DOMCryptoContext.setIdAttributeNS()
permalink: Java/DOMCryptoContext/setIdAttributeNS
date: 2021-01-04
key: JavaJava.D.DOMCryptoContext
category: java
tags: ['java se', 'javax.xml.crypto.dom', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DOMCryptoContext.metodos valor="setIdAttributeNS" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setIdAttributeNS(Element element, String namespaceURI, String localName)
~~~

## Parámetros
* **String localName**,  {% include w3api/param_description.html metodo=_data parametro="String localName" %}
* **String namespaceURI**,  {% include w3api/param_description.html metodo=_data parametro="String namespaceURI" %}
* **Element element**,  {% include w3api/param_description.html metodo=_data parametro="Element element" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DOMCryptoContext](/Java/DOMCryptoContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DOMCryptoContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
