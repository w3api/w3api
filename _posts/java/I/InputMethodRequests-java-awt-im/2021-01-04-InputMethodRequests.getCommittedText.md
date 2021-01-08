---
title: InputMethodRequests.getCommittedText()
permalink: Java/InputMethodRequests-java-awt-im/getCommittedText
date: 2021-01-04
key: JavaJava.I.InputMethodRequests-java-awt-im
category: java
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
* **int endIndex**,  {% include w3api/param_description.html metodo=_data parametro="int endIndex" %}
* **int beginIndex**,  {% include w3api/param_description.html metodo=_data parametro="int beginIndex" %}
* **AttributedCharacterIterator.Attribute[] attributes**,  {% include w3api/param_description.html metodo=_data parametro="AttributedCharacterIterator.Attribute[] attributes" %}

## Clase Padre
[InputMethodRequests](/Java/InputMethodRequests-java-awt-im/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InputMethodRequests-java-awt-im.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
