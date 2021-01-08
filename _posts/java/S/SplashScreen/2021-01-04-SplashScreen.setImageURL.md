---
title: SplashScreen.setImageURL()
permalink: Java/SplashScreen/setImageURL
date: 2021-01-04
key: JavaJava.S.SplashScreen
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SplashScreen.metodos valor="setImageURL" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setImageURL(URL imageURL) throws NullPointerException, IOException, IllegalStateException
~~~

## Parámetros
* **URL imageURL**,  {% include w3api/param_description.html metodo=_data parametro="URL imageURL" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[SplashScreen](/Java/SplashScreen/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SplashScreen.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
