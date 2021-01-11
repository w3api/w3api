---
title: Marshaller.setAdapter()
permalink: Java/Marshaller/setAdapter
date: 2021-01-11
key: JavaJava.M.Marshaller
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.Marshaller.metodos valor="setAdapter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<A extends XmlAdapter>void setAdapter(Class<A> type, A adapter)
void setAdapter(XmlAdapter adapter)
~~~

## Parámetros
* **XmlAdapter adapter**,  {% include w3api/param_description.html metodo=_dato parametro="XmlAdapter adapter" %}
* **A adapter**,  {% include w3api/param_description.html metodo=_dato parametro="A adapter" %}
* **Class&lt;A&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="Class<A> type" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[Marshaller](/Java/Marshaller/)

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
