---
title: Marshaller.getAdapter()
permalink: Java/Marshaller/getAdapter
date: 2021-01-04
key: JavaJava.M.Marshaller
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.Marshaller.metodos valor="getAdapter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<A extends XmlAdapter>A getAdapter(Class<A> type)
~~~

## Parámetros
* **Class&lt;A&gt; type**,  {% include w3api/param_description.html metodo=_data parametro="Class<A> type" %}

## Clase Padre
[Marshaller](/Java/Marshaller/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.Marshaller.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
