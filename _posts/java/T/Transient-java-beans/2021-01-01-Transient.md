---
title: Transient
permalink: Java/Transient-java-beans
date: 2021-01-11
key: JavaJava.T.Transient-java-beans
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'anotacion java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.Transient-java-beans.description }}

## Sintaxis
~~~java
@Target(METHOD) @Retention(RUNTIME) public @interface Transient
~~~

## Elementos
* [value](/Java/Transient-java-beans/value)

## Ejemplo
~~~java
{{ site.data.Java.T.Transient-java-beans.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.Transient-java-beans.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
