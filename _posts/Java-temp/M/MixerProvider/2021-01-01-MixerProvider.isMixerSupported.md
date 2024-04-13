---
title: MixerProvider.isMixerSupported()
permalink: /Java/MixerProvider/isMixerSupported/
date: 2021-01-11
key: Java.M.MixerProvider
category: Java
tags: ['java se', 'javax.sound.sampled.spi', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MixerProvider.metodos valor="isMixerSupported" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean isMixerSupported(Mixer.Info info)
~~~

## Parámetros
* **Mixer.Info info**,  {% include w3api/param_description.html metodo=_dato parametro="Mixer.Info info" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MixerProvider](/Java/MixerProvider/)

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
