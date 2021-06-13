---
title: RespectBinding
permalink: Java/RespectBinding
date: 2021-01-11
key: Java.R.RespectBinding
category: java
tags: ['java se', 'javax.xml.ws', 'java.xml.ws', 'anotacion java', 'Java 1.6', 'JAX-WS 2.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RespectBinding.description }}

## Sintaxis
~~~java
@Target({TYPE,METHOD,FIELD}) @Retention(RUNTIME) @Documented @WebServiceFeatureAnnotation(id="javax.xml.ws.RespectBindingFeature", bean=RespectBindingFeature.class) public @interface RespectBinding
~~~

## Elementos
* [enabled](/Java/RespectBinding/enabled)

## Ejemplo
~~~java
{{ site.data.Java.R.RespectBinding.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RespectBinding.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
