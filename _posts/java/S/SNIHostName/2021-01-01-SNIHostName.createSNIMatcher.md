---
title: SNIHostName.createSNIMatcher()
permalink: Java/SNIHostName/createSNIMatcher
date: 2021-01-11
key: JavaJava.S.SNIHostName
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SNIHostName.metodos valor="createSNIMatcher" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static SNIMatcher createSNIMatcher(String regex)
~~~

## Parámetros
* **String regex**,  {% include w3api/param_description.html metodo=_dato parametro="String regex" %}

## Excepciones
[PatternSyntaxException](/Java/PatternSyntaxException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SNIHostName](/Java/SNIHostName/)

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
