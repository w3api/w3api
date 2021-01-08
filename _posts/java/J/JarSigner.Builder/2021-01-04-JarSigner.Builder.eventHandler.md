---
title: JarSigner.Builder.eventHandler()
permalink: Java/JarSigner/Builder/eventHandler
date: 2021-01-04
key: JavaJava.J.JarSigner.Builder
category: java
tags: ['java se', 'jdk.security.jarsigner', 'jdk.jartool', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JarSigner.Builder.metodos valor="eventHandler" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JarSigner.Builder eventHandler(BiConsumer<String,String> handler)
~~~

## Parámetros
* **String&gt; handler**,  {% include w3api/param_description.html metodo=_data parametro="String> handler" %}
* **BiConsumer&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="BiConsumer<String" %}

## Clase Padre
[JarSigner.Builder](/Java/JarSigner/Builder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JarSigner.Builder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
