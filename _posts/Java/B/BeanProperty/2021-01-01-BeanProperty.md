---
title: BeanProperty
permalink: /Java/BeanProperty/
date: 2021-01-11
key: Java.B.BeanProperty
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BeanProperty.description }}

## Sintaxis
~~~java
@Documented @Target(METHOD) @Retention(RUNTIME) public @interface BeanProperty
~~~

## Elementos
* [bound](/Java/BeanProperty/bound/)
* [description](/Java/BeanProperty/description/)
* [enumerationValues](/Java/BeanProperty/enumerationValues/)
* [expert](/Java/BeanProperty/expert/)
* [hidden](/Java/BeanProperty/hidden/)
* [preferred](/Java/BeanProperty/preferred/)
* [required](/Java/BeanProperty/required/)
* [visualUpdate](/Java/BeanProperty/visualUpdate/)

## Ejemplo
~~~java
{{ site.data.Java.B.BeanProperty.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BeanProperty.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
