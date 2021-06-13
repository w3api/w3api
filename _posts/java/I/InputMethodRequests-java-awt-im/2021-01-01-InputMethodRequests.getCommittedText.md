---
title: InputMethodRequests.getCommittedText()
permalink: /Java/InputMethodRequests-java-awt-im/getCommittedText/
date: 2021-01-11
key: Java.I.InputMethodRequests-java-awt-im
category: Java
tags: ['java se', 'java.awt.im', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InputMethodRequests-java-awt-im.metodos valor="getCommittedText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
AttributedCharacterIterator getCommittedText(int beginIndex, int endIndex, AttributedCharacterIterator.Attribute[] attributes)
~~~

## Parámetros
* **AttributedCharacterIterator.Attribute[] attributes**,  {% include w3api/param_description.html metodo=_dato parametro="AttributedCharacterIterator.Attribute[] attributes" %}
* **int beginIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int beginIndex" %}
* **int endIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int endIndex" %}

## Clase Padre
[InputMethodRequests](/Java/InputMethodRequests-java-awt-im/)

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
