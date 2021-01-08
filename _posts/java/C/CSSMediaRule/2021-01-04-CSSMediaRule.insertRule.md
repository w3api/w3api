---
title: CSSMediaRule.insertRule()
permalink: Java/CSSMediaRule/insertRule
date: 2021-01-04
key: JavaJava.C.CSSMediaRule
category: java
tags: ['java se', 'org.w3c.dom.css', 'jdk.xml.dom', 'metodo java', 'Java 1.4', 'DOM Level 2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CSSMediaRule.metodos valor="insertRule" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int insertRule(String rule, int index) throws DOMException
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **String rule**,  {% include w3api/param_description.html metodo=_data parametro="String rule" %}

## Excepciones
[DOMException](/Java/DOMException/)

## Clase Padre
[CSSMediaRule](/Java/CSSMediaRule/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CSSMediaRule.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
