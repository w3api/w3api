---
title: DOMCryptoContext.setIdAttributeNS()
permalink: /Java/DOMCryptoContext/setIdAttributeNS/
date: 2021-01-11
key: Java.D.DOMCryptoContext
category: Java
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
* **Element element**,  {% include w3api/param_description.html metodo=_dato parametro="Element element" %}
* **String namespaceURI**,  {% include w3api/param_description.html metodo=_dato parametro="String namespaceURI" %}
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DOMCryptoContext](/Java/DOMCryptoContext/)

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
